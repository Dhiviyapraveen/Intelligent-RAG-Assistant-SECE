import { useState } from "react";
import { askQuestion } from "../services/api";
import Navbar from "../components/Navbar/Navbar";

function Home() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!question.trim()) return;

    const userQuestion = question;

    // Add user message
    setMessages((prev) => [
      ...prev,
      {
        type: "user",
        text: userQuestion,
      },
    ]);

    setQuestion("");
    setLoading(true);

    const response = await askQuestion(userQuestion);

    // Add bot response
    setMessages((prev) => [
      ...prev,
      {
        type: "bot",
        text: response.answer,
        sources: response.sources,
      },
    ]);

    setLoading(false);
  };

  return (
    <div>
      <Navbar />

      <div>
        {messages.map((message, index) => (
          <div key={index}>
            <h4>{message.type === "user" ? "You" : "Assistant"}</h4>

            <p>{message.text}</p>

            {message.type === "bot" &&
              message.sources &&
              message.sources.length > 0 && (
                <>
                  <h5>Sources</h5>

                  <ul>
                    {message.sources.map((source, i) => (
                      <li key={i}>
                        <a
                          href={source.url}
                          target="_blank"
                          rel="noreferrer"
                        >
                          {source.title}
                        </a>
                      </li>
                    ))}
                  </ul>
                </>
              )}
          </div>
        ))}
      </div>

      {loading && <p>Generating response...</p>}

      <input
        type="text"
        placeholder="Ask anything about SECE..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();
          }
        }}
      />

      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default Home;