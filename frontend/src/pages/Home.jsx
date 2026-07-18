import { useState } from "react";

import Sidebar from "../components/Sidebar/Sidebar";
import Navbar from "../components/Navbar/Navbar";
import ChatBox from "../components/ChatBox/ChatBox";
import ChatInput from "../components/ChatInput/ChatInput";

import { askQuestion } from "../services/api";

function Home() {
  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const [chats, setChats] = useState([]);

  const [currentChat, setCurrentChat] = useState(null);

  const handleNewChat = () => {
    setMessages([]);
    setQuestion("");
    setCurrentChat(null);
  };

  const handleSend = async () => {
    if (!question.trim()) return;

    const userQuestion = question;

    if (messages.length === 0) {
      const newChat = {
        id: Date.now(),
        title:
          userQuestion.length > 30
            ? userQuestion.substring(0, 30) + "..."
            : userQuestion,
      };

      setChats((prev) => [newChat, ...prev]);

      setCurrentChat(newChat.id);
    }

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
    <div
      style={{
        display: "flex",
        height: "100vh",
      }}
    >
      <Sidebar
        chats={chats}
        currentChat={currentChat}
        onNewChat={handleNewChat}
        onSelectChat={setCurrentChat}
      />

      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
        }}
      >
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
      </div>
    </div>
  );
}

export default Home;