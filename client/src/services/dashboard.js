import api from "./api";

export const getSummary = async () => {
  const res = await api.get("/dashboard/summary");
  return res.data;
};

export const getMonthly = async () => {
  const res = await api.get("/dashboard/monthly");
  return res.data;
};

export const getRecent = async () => {
  const res = await api.get("/dashboard/recent");
  return res.data;
};

export const getCategory = async () => {
  const res = await api.get("/dashboard/category");
  return res.data;
};

export const getTrend = async () => {
  const res = await api.get("/dashboard/trend");
  return res.data;
};