import api from "./api";

export const register = async (user) => {
  const response = await api.post("/users/register", user);
  return response.data;
};

export const login = async (email, password) => {
  const form = new URLSearchParams();

  form.append("username", email);
  form.append("password", password);

  const response = await api.post("/users/login", form, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });

  localStorage.setItem("token", response.data.access_token);

  return response.data;
};

export const getCurrentUser = async () => {
  const response = await api.get("/users/me");
  return response.data;
};

export const logout = () => {
  localStorage.removeItem("token");
};

export const isLoggedIn = () => {
  return !!localStorage.getItem("token");
};