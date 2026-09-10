import './App.css'

function App() {

  return (
  <main className="app">
    <header>
      <h1>Job Searcher</h1>
      <p>Relevant jobs without the noise.</p>
    </header>

    <section className="stats">
      <div className="stat-card">
        <span>Matches today</span>
        <strong> 0</strong>
      </div>

      <div className="stat-card">
        <span>New jobs</span>
        <strong> 0</strong>
      </div>

      <div className="stat-card">
        <span>Companies</span>
        <strong> 0</strong>
      </div>
    </section>

    <section className="jobs">
      <div className="jobs-header">
        <h2>Recent jobs</h2>
        <button type="button">Refresh</button>
      </div>

      <div className="empty-state">
        <h3>No relevant jobs yet</h3>
        <p>New matching vacancies will appear here.</p>
      </div>
    </section>
  </main>
)
}

export default App