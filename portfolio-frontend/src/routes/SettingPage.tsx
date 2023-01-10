import {
  Avatar,
  Box,
  Button,
  Container,
  Divider,
  FormControl,
  FormLabel,
  Heading,
  HStack,
  Input,
  VStack,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import useUser from "../lib/useUser";

export default function SettingPage() {
  const { register, handleSubmit } = useForm();
  const { user } = useUser();
  return (
    <Box
      pb={40}
      mt={10}
      px={{
        base: 10,
        lg: 40,
      }}
    >
      <Container pt="200px">
        <Heading textAlign={"center"} color="white">
          프로필 수정
        </Heading>
        <HStack>
          <VStack spacing={5} mt={10}>
            <FormControl>
              <VStack>
                <Avatar size="mg" />
                <FormLabel
                  display="inline"
                  border="1px"
                  p="10px"
                  color="whitesmoke"
                  cursor="pointer"
                >
                  이미지 변경
                </FormLabel>
                <Input
                  {...register("file")}
                  type="file"
                  accept="image/*"
                  position="absolute"
                  w="1px"
                  h="1px"
                  border="0"
                  p="0"
                  m="-1px"
                  overflow="hidden"
                />
              </VStack>
            </FormControl>
          </VStack>
          <FormControl>
            <FormLabel fontSize="lg" textColor="white">
              {user?.name}
            </FormLabel>
            <Input
              {...register("name")}
              size="lg"
              placeholder="변경할 이름"
              color="white"
            />
          </FormControl>
        </HStack>
        <Divider mt="20px" mb="20px" color="white" />
        <Button left="20px" colorScheme="red">
          완료
        </Button>
      </Container>
    </Box>
  );
}
