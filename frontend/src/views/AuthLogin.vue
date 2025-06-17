<template>
  <div class="auth-popup">
    <div class="auth-container">
      <div class="auth-header">
        <h2>Sign In to SkyNova</h2>
        <p>Welcome back! Please sign in to your account.</p>
      </div>

      <form @submit.prevent="handleLogin" class="auth-form">
        <div class="form-group">
          <label for="email">Email Address</label>
          <input
            type="email"
            id="email"
            v-model="form.email"
            :class="{ 'error': errors.email }"
            placeholder="Enter your email"
            required
          />
          <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="form.password"
            :class="{ 'error': errors.password }"
            placeholder="Enter your password"
            required
          />
          <span v-if="errors.password" class="error-message">{{ errors.password }}</span>
        </div>

        <div v-if="generalError" class="alert alert-error">
          {{ generalError }}
          <button 
            v-if="needsVerification" 
            @click="resendVerification" 
            type="button" 
            class="btn-link"
            :disabled="resendLoading"
          >
            {{ resendLoading ? 'Sending...' : 'Resend verification email' }}
          </button>
        </div>

        <div v-if="successMessage" class="alert alert-success">
          {{ successMessage }}
        </div>

        <button type="submit" class="btn-primary" :disabled="loading">
          {{ loading ? 'Signing In...' : 'Sign In' }}
        </button>
      </form>

      <div class="auth-footer">
        <p>Don't have an account? 
          <a href="#" @click.prevent="switchToSignup">Sign up here</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import AuthService from '../services/auth.js'

export default {
  name: 'AuthLogin',
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      errors: {},
      generalError: '',
      successMessage: '',
      needsVerification: false,
      loading: false,
      resendLoading: false
    }
  },
  methods: {
    async handleLogin() {
      this.loading = true
      this.errors = {}
      this.generalError = ''
      this.needsVerification = false

      try {
        const result = await AuthService.login(this.form.email, this.form.password)
        
        if (result.success) {
          // Send success message to parent window
          window.opener.postMessage({
            type: 'AUTH_SUCCESS',
            user: result.user
          }, window.location.origin)
        }
      } catch (error) {
        if (error.errors) {
          this.errors = error.errors
        } else {
          this.generalError = error.error || 'Login failed'
          this.needsVerification = error.needs_verification || false
        }
      } finally {
        this.loading = false
      }
    },

    async resendVerification() {
      if (!this.form.email) {
        this.generalError = 'Please enter your email address first'
        return
      }

      this.resendLoading = true
      try {
        const result = await AuthService.resendVerification(this.form.email)
        this.successMessage = result.message
        this.generalError = ''
      } catch (error) {
        this.generalError = error.error || 'Failed to send verification email'
      } finally {
        this.resendLoading = false
      }
    },

    switchToSignup() {
      // Redirect to signup page in the same popup
      this.$router.push('/auth/signup')
    }
  }
}
</script>

<style scoped>
.auth-popup {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #2a2a2b 0%, #9c9ca2 100%);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.auth-container {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.auth-header {
  text-align: center;
  margin-bottom: 2rem;
}

.auth-header h2 {
  color: #1a202c;
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.auth-header p {
  color: #718096;
  font-size: 0.875rem;
}

.auth-form {
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  color: #374151;
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.form-group input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.875rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-group input.error {
  border-color: #ef4444;
}

.error-message {
  color: #ef4444;
  font-size: 0.75rem;
  margin-top: 0.25rem;
  display: block;
}

.alert {
  padding: 0.75rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  font-size: 0.875rem;
}

.alert-error {
  background-color: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
}

.alert-success {
  background-color: #f0fdf4;
  color: #16a34a;
  border: 1px solid #bbf7d0;
}

.btn-primary {
  width: 100%;
  background: linear-gradient(135deg, #9c9ca2 0%, #2a2a2b 100%);
  color: white;
  border: none;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: opacity 0.15s ease-in-out;
}

.btn-primary:hover:not(:disabled) {
  opacity: 0.9;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-link {
  background: none;
  border: none;
  color: #667eea;
  text-decoration: underline;
  cursor: pointer;
  font-size: 0.875rem;
  margin-left: 0.5rem;
}

.btn-link:hover:not(:disabled) {
  color: #5a67d8;
}

.btn-link:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.auth-footer {
  text-align: center;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}

.auth-footer p {
  color: #6b7280;
  font-size: 0.875rem;
}

.auth-footer a {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
}

.auth-footer a:hover {
  text-decoration: underline;
}
</style> 