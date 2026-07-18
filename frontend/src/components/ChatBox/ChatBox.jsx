import { useEffect, useRef } from "react";

import "./ChatBox.css";

import Message from "../Message/Message";
import Loading from "../Loading/Loading";

function ChatBox({ messages, loading }) {

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  return (
    <div className="chatbox">

      {messages.length === 0 && (
        <div className="welcome">
          <h2>🎓 SECE Intelligent RAG Assistant</h2>

          <p>
            Ask anything about Sri Eshwar College of Engineering.
          </p>
        </div>
      )}

      {messages.map((message, index) => (
        <Message
          key={index}
          message={message}
        />
      ))}

      {loading && <Loading />}

      <div ref={bottomRef}></div>

    </div>
  );
}

export default ChatBox;