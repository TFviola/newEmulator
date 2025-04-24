import express from 'express';
import cors from 'cors';

const app = express();
const port = 3001;

// Enable CORS for all routes
app.use(cors());
app.use(express.json());

// Singleton Session Manager
class ServerSessionManager {
    constructor() {
        if (ServerSessionManager.instance) {
            return ServerSessionManager.instance;
        }
        ServerSessionManager.instance = this;
        this.isNegativeForm = false;
    }

    getFormState() {
        return this.isNegativeForm;
    }

    setFormState(isNegative) {
        this.isNegativeForm = isNegative;
    }
}

// Create the singleton instance
const sessionManager = new ServerSessionManager();

// GET endpoint to retrieve the toggle state
app.get('/api/toggle-state', (req, res) => {
    res.json({ isNegativeForm: sessionManager.getFormState() });
});

// POST endpoint to update the toggle state
app.post('/api/toggle-state', (req, res) => {
    sessionManager.setFormState(req.body.isNegativeForm);
    res.json({ isNegativeForm: sessionManager.getFormState() });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
}); 