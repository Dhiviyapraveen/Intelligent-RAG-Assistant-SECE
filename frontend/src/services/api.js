import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const askQuestion = async (question) => {
  try {
    const response = await api.post("/chat/", {
      question: question,
    });

    return response.data;
  } catch (error) {
    console.error("API Error:", error);

    return {
      answer: "Unable to connect to the backend.",
      sources: [],
    };
  }
};

export default api;