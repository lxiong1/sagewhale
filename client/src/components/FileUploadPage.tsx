import { Box, Image } from "@chakra-ui/react";
import FileUploadButton from "./FileUploadButton";
import sagewhale from "../images/sagewhale-logo.png";
import TypeWriterEffect from "./TypeWriterEffect";

function FileUploadPage() {
  return (
    <div>
      <Box boxSize="container.md" textAlign={"center"}>
        <Image src={sagewhale} alt="Sagewhale" />
        <TypeWriterEffect />
        <FileUploadButton />
      </Box>
    </div>
  );
}

export default FileUploadPage;
