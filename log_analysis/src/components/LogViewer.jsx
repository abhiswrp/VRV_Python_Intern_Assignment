import React, { useState, useEffect } from 'react';
import axios from 'axios';

function LogViewer() {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:5000/api/logs')
      .then(response => {
        setLogs(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching logs:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading logs...</div>;
  }

  return (
    <div className="log-viewer">
      <h2>Logs</h2>
      <ul>
        {logs.map((log, index) => (
          <li key={index}>
            <p>{log}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default LogViewer;
