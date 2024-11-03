import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'
import SliderComponent from './SliderComponent'

function App() {
  const [text, setText] = useState('')
  const [wordCount, setWordCount] = useState(0)
  const [score, setScore] = useState(null)

  const handleTextChange = (event) => setText(event.target.value)

  useEffect(() => {
    setWordCount(text.trim() ? text.trim().split(/\s+/).length : 0)
  }, [text])

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/predict', {
        text: text,
      })
      const aiScore = response.data.score  // Convert to percentage
      setScore(aiScore)
    } catch (error) {
      console.log(error.message)
    }
  }

  return (
    <div className="container">
      <nav className="navbar">
        <h1 className="logo">AiVsHuman</h1>
        <ul className="nav-links">
          <li>Home</li>
          <li>About Us</li>
          <li>Contributors</li>
        </ul>
      </nav>

      <header className="header">
        <h2>Detect the AI content in your text</h2>
      </header>

      <main className="main-content">
        <textarea
          placeholder="Write your text here..."
          value={text}
          onChange={handleTextChange}
        />
        <p className="word-count">Word Count: {wordCount}</p>

        <button className="upload-button" onClick={handleSubmit}>
          Upload
        </button>

        {score !== null && (
          <div>
            <p>AI Detection Score: {score}%</p>
            <SliderComponent percentage={score} />
          </div>
        )}
      </main>
    </div>
  )
}

export default App
