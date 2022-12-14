import { ChakraProvider, VStack, Grid, theme } from "@chakra-ui/react";
import { ColorModeSwitcher } from "./ColorModeSwitcher";
import FileUploadPage from "./components/FileUploadPage";

export const App = () => (
  <ChakraProvider theme={theme}>
    <Grid minH="100vh" p={3}>
      <ColorModeSwitcher justifySelf="flex-end" />
      <VStack>
        <FileUploadPage />
      </VStack>
    </Grid>
  </ChakraProvider>
);
