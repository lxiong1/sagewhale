import { Button, Text } from "@chakra-ui/react";

const FileUploadButton = function () {
  return (
    <Button
      colorScheme="alphaBlack"
      variant={"outline"}
      size={"lg"}
      _hover={{ bg: "#eeeeee" }}
    >
      <Text as={"b"}>Upload File</Text>
    </Button>
  );
};

export default FileUploadButton;
