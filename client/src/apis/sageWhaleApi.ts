import axios from "axios";

const SUBSCRIBER_INFO_ROUTE = "/subscriber_info";
const UPLOAD_JSON_ROUTE = `${SUBSCRIBER_INFO_ROUTE}/upload/json`;

const sageWhaleApi = axios.create({
  baseURL: process.env.REACT_APP_SAGEWHALE_API_URL,
});

const getAllSubscriberInfo = function () {
  return sageWhaleApi.get(SUBSCRIBER_INFO_ROUTE);
};

const postJsonFile = function (formData: FormData) {
  return sageWhaleApi.post(UPLOAD_JSON_ROUTE, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

export default { getAllSubscriberInfo, postJsonFile };
