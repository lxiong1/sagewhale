import { Button, Text } from "@chakra-ui/react";
import { useDropzone } from "react-dropzone";
import { useEffect } from "react";
import { postJsonFile } from "../apis/sageWhaleApi";
import useApi from "../hooks/useApi";

const FileUploadButton = function () {
  const jsonFiles = useApi(postJsonFile);
  let formData = new FormData();

  const { acceptedFiles, getRootProps, getInputProps } = useDropzone({
    multiple: false,
    accept: {
      "application/json": [".json"],
    },
  });

  acceptedFiles.map((file) => {
    formData.append("file", file, file.name);
  });

  useEffect(() => {
    jsonFiles.request(formData);
  }, []);

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
