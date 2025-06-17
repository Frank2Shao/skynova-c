// Authentication service for popup login functionality
import axios from 'axios'

const API_BASE = '/api'  // Use relative URL since frontend is served by Django

// Configure axios defaults
axios.defaults.withCredentials = true

// Function to get CSRF token from cookies
function getCsrfToken() {
  const name = 'csrftoken'
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

// Set up axios interceptor to include CSRF token
axios.interceptors.request.use(function (config) {
  const csrfToken = getCsrfToken()
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken
  }
  return config
}, function (error) {
  return Promise.reject(error)
})

class AuthService {
  constructor() {
    this.popupWindow = null
    this.popupCheckInterval = null
    this.initCSRF()
  }

  // Initialize CSRF token
  async initCSRF() {
    try {
      await axios.get(`${API_BASE}/auth/csrf/`)
    } catch (error) {
      console.warn('Failed to initialize CSRF token:', error)
    }
  }

  // Open popup window for authentication
  openAuthPopup(mode = 'login') {
    const width = 480
    const height = 600
    const left = (screen.width - width) / 2
    const top = (screen.height - height) / 2

    const popupUrl = mode === 'login' ? '/auth/login' : '/auth/signup'
    
    this.popupWindow = window.open(
      popupUrl,
      'authPopup',
      `width=${width},height=${height},left=${left},top=${top},scrollbars=no,resizable=no,menubar=no,toolbar=no,location=no,status=no`
    )

    return new Promise((resolve, reject) => {
      // Check if popup is closed
      this.popupCheckInterval = setInterval(() => {
        if (this.popupWindow.closed) {
          clearInterval(this.popupCheckInterval)
          reject(new Error('Popup was closed by user'))
        }
      }, 1000)

      // Listen for messages from popup
      const messageHandler = (event) => {
        if (event.origin !== window.location.origin) return

        if (event.data.type === 'AUTH_SUCCESS') {
          clearInterval(this.popupCheckInterval)
          window.removeEventListener('message', messageHandler)
          this.popupWindow.close()
          resolve(event.data.user)
        } else if (event.data.type === 'AUTH_ERROR') {
          clearInterval(this.popupCheckInterval)
          window.removeEventListener('message', messageHandler)
          this.popupWindow.close()
          reject(new Error(event.data.error))
        }
      }

      window.addEventListener('message', messageHandler)
    })
  }

  // API calls
  async signup(email, password1, password2) {
    try {
      const response = await axios.post(`${API_BASE}/auth/signup/`, {
        email,
        password1,
        password2
      })
      return response.data
    } catch (error) {
      throw error.response?.data || { error: 'Network error' }
    }
  }

  async login(email, password) {
    try {
      const response = await axios.post(`${API_BASE}/auth/login/`, {
        email,
        password
      })
      return response.data
    } catch (error) {
      throw error.response?.data || { error: 'Network error' }
    }
  }

  async logout() {
    try {
      const response = await axios.post(`${API_BASE}/auth/logout/`)
      return response.data
    } catch (error) {
      throw error.response?.data || { error: 'Network error' }
    }
  }

  async getUserStatus() {
    try {
      const response = await axios.get(`${API_BASE}/auth/status/`)
      return response.data
    } catch (error) {
      throw error.response?.data || { error: 'Network error' }
    }
  }

  async resendVerification(email) {
    try {
      const response = await axios.post(`${API_BASE}/auth/resend-verification/`, {
        email
      })
      return response.data
    } catch (error) {
      throw error.response?.data || { error: 'Network error' }
    }
  }
}

export default new AuthService() 