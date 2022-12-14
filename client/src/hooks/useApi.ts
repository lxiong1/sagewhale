import { useState } from "react";

const useApi = function (apiFunction: any) {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const request = async function (...args: any) {
    setLoading(true);
    try {
      const result = await apiFunction(...args);
      setData(result.data);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      }

      setError("Unknown Error Occurred");
    } finally {
      setLoading(false);
    }
  };

  return {
    data,
    error,
    loading,
    request,
  };
};

export default useApi;
