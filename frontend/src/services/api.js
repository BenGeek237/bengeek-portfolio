import axios from 'axios'

// Configuration d'axios pour communiquer avec le backend Django
const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api',
    headers: {
        'Content-Type': 'application/json',
    },
})

// Service pour les projets
export const projectService = {
    async getAllProjects() {
        const response = await apiClient.get('/projects/projects/')
        return response.data
    },

    async getFeaturedProjects() {
        const response = await apiClient.get('/projects/projects/?featured=true')
        return response.data
    },

    async getProjectBySlug(slug) {
        const response = await apiClient.get(`/projects/projects/?slug=${slug}`)
        return response.data.results[0]
    },
}

// Service pour le blog
export const blogService = {
    async getAllPosts() {
        const response = await apiClient.get('/blog/posts/')
        return response.data
    },

    async getLatestPosts(limit = 3) {
        const response = await apiClient.get(`/blog/posts/?ordering=-published_date&limit=${limit}`)
        return response.data
    },

    async getPostBySlug(slug) {
        const response = await apiClient.get(`/blog/posts/?slug=${slug}`)
        // Gérer différentes structures de réponse
        if (response.data) {
            // Si c'est un tableau
            if (Array.isArray(response.data)) {
                return response.data[0] || null
            }
            // Si c'est un objet avec results
            if (response.data.results && Array.isArray(response.data.results)) {
                return response.data.results[0] || null
            }
            // Si c'est directement l'objet
            if (response.data.slug === slug) {
                return response.data
            }
        }
        return null
    },

    async getCategories() {
        const response = await apiClient.get('/blog/categories/')
        return response.data
    },

    async incrementViews(postId) {
        const response = await apiClient.post(`/blog/posts/${postId}/increment_views/`)
        return response.data
    },
}

export default apiClient