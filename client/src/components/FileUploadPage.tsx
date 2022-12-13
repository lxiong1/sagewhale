import { Box, Image } from "@chakra-ui/react";
import FileUploadButton from "./FileUploadButton";
import sagewhale from "../images/sagewhale-logo.png";

function FileUploadPage() {
  return (
    <div>
      <Box boxSize="container.md" textAlign={"center"}>
        <Image src={sagewhale} alt="Sagewhale" />
        <FileUploadButton />
      </Box>
    </div>
  );
}

export default FileUploadPage;
