import { Button, Text } from "@chakra-ui/react";
import { useDropzone } from "react-dropzone";
import { useEffect } from "react";
import postJsonFiles from "../apis/sageWhaleApi";
import useApi from "../hooks/useApi";

const FileUploadButton = function () {
  const jsonFiles = useApi(postJsonFiles);
  let formData = new FormData();

  const { acceptedFiles, getRootProps, getInputProps } = useDropzone({
    multiple: false,
    accept: {
      "application/json": [".json"],
    },
  });

  acceptedFiles.map((file) => {
    console.log(file);
    formData.append("file", file, file.name);
    console.log(formData.get("file"));
    console.log(process.env.SAGEWHALE_API_URL);
  });

  useEffect(() => {
    jsonFiles.request(formData);
  }, []);

  console.log(jsonFiles.error)
  console.log(jsonFiles.data)

  return (
    <div {...getRootProps({ className: "dropzone" })}>
      <input {...getInputProps()} />
      <Button
        colorScheme="alphaBlack"
        variant={"outline"}
        size={"lg"}
        _hover={{ bg: "#eeeeee" }}
      >
        <Text as={"b"}>Upload File</Text>
      </Button>
    </div>
  );
};

export default FileUploadButton;
