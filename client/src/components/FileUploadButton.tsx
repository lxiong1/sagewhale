import { Button, Text } from "@chakra-ui/react";
import Dropzone from "react-dropzone";

const FileUploadButton = function () {
  const onDrop = (acceptedFiles: any) => {
    console.log(acceptedFiles);
  };

  return (
    <Dropzone onDrop={onDrop}>
      {({ getRootProps, getInputProps }) => (
        <div {...getRootProps()}>
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
      )}
    </Dropzone>
  );
};

export default FileUploadButton;
