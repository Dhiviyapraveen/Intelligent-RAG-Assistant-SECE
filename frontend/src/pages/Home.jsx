import { useState } from "react";

import Navbar from "../components/Navbar/Navbar";
import ChatBox from "../components/ChatBox/ChatBox";
import ChatInput from "../components/ChatInput/ChatInput";

import { askQuestion } from "../services/api";

function Home() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!question.trim()) return;

    const userQuestion = question;

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
    <>
      <Navbar />

      <ChatBox
        messages={messages}
        loading={loading}
      />

      <ChatInput
        question={question}
        setQuestion={setQuestion}
        handleSend={handleSend}
      />
    </>
  );
}

export default Home;