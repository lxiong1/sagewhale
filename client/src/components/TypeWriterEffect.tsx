import { Box, Text } from "@chakra-ui/react";
import Typewriter from "typewriter-effect";

const TypeWriterEffect = function () {
  return (
    <Box p={5}>
      <Text fontSize="3xl" as={"b"}>
        <Typewriter
          onInit={(typewriter) => {
            typewriter
              .typeString(
                `<span style="color: #2645bd;">Sagewhale</span>, Your <span style="color: #2645bd;">Visualization</span> Tool`
              )
              .start();
          }}
        />
      </Text>
    </Box>
  );
};

export default TypeWriterEffect;
