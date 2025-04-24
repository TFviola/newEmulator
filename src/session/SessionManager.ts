class SessionManager {
    private static instance: SessionManager;
    private isNegativeForm: boolean = false;
    private serverUrl: string = 'http://localhost:3001/api';

    private constructor() {
        // Initialize state from server
        this.fetchStateFromServer();
    }

    public static getInstance(): SessionManager {
        if (!SessionManager.instance) {
            SessionManager.instance = new SessionManager();
        }
        return SessionManager.instance;
    }

    public getFormState(): boolean {
        return this.isNegativeForm;
    }

    public setFormState(isNegative: boolean): void {
        this.isNegativeForm = isNegative;
        // Update server state
        this.updateServerState(isNegative);
    }

    private async fetchStateFromServer(): Promise<void> {
        try {
            const response = await fetch(`${this.serverUrl}/toggle-state`);
            const data = await response.json();
            this.isNegativeForm = data.isNegativeForm;
        } catch (error) {
            console.error('Error fetching state from server:', error);
        }
    }

    private async updateServerState(isNegative: boolean): Promise<void> {
        try {
            await fetch(`${this.serverUrl}/toggle-state`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ isNegativeForm: isNegative }),
            });
        } catch (error) {
            console.error('Error updating state on server:', error);
        }
    }
}

export default SessionManager; 