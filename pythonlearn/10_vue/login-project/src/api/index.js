import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8888'; // 替换为实际的后端 API 地址

export const loginUser = async (username, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/login/`, { username, password });
    console.log(response.data);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const registerUser = async (username, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/register/`, { username, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};