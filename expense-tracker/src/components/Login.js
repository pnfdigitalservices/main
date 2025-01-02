import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import '../css/Login.css'; // Import your CSS file

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        try {
            const response = await axios.post('http://localhost:5000/login', { username, password });
            if (response.data.message === 'Login successful') {
                localStorage.setItem('isAuthenticated', 'true');
                localStorage.setItem('isAdmin', response.data.isAdmin);
                localStorage.setItem('username', username);
                navigate(response.data.isAdmin ? '/admin-dashboard' : '/user-dashboard');
            } else {
                setError('Invalid username or password.');
            }
        } catch (error) {
            console.error('Login error:', error);
            setError('An error occurred during login.');
        }
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <h2>Login</h2>
                {error && <div className="error-message">{error}</div>}
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="username">Username:</label>
                        <input
                            type="text"
                            id="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password:</label>
                        <input
                            type="password"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    <button type="submit" className="submit-button">Log In</button>
                    <div className="bottom-links">
                        <Link to="/forgot-password">Forgot Password?</Link>
                        <Link to="/signup">Sign Up</Link>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Login;