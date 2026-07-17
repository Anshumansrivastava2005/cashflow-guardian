import api from "./api";

export const getPrediction = async (userId) => {
  const res = await api.get(`/ai/predict/${userId}`);
  return res.data;
};

export const getAdvice = async (userId) => {
  const res = await api.get(`/ai/advice/${userId}`);
  return res.data;
};

export const getRisk = async (userId) => {
  const res = await api.get(`/ai/risk/${userId}`);
  return res.data;
};