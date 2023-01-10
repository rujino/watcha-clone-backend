import {
  Avatar,
  Box,
  Button,
  HStack,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
  Stack,
} from "@chakra-ui/react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { logOut } from "../api";
import useUser from "../lib/useUser";

export default function Header() {
  const { userLoading, isLoggedIn, user } = useUser();
  const queryClinet = useQueryClient();
  const navigator = useNavigate();
  const mutation = useMutation(logOut, {
    onSuccess: (data) => {
      console.log(data);
      queryClinet.refetchQueries(["me"]);
      queryClinet.refetchQueries(["series"]);
    },
  });
  const onMe = () => {
    navigator("me/");
  };
  const onLogOut = () => {
    mutation.mutate();
    navigator("/user/log-in/");
  };
  const onClickLogin = () => {
    navigator("/user/log-in/");
  };
  const onClickSignin = () => {
    navigator("/user/sign-in/");
  };
  const onClickSetting = () => {
    navigator("/setting/");
  };
  return (
    <Stack position="fixed" left="0" top="0" w="100%" zIndex="500">
      <HStack h="56px" bg="#141517" justifyContent="space-between">
        <Box border="1px">logo</Box>
        <Box border="1px">
          {!userLoading ? (
            !isLoggedIn ? (
              <>
                <Button onClick={onClickLogin}>Log in</Button>
                <Button onClick={onClickSignin}>Sign in</Button>
              </>
            ) : (
              <Menu>
                <MenuButton marginRight="50px">
                  <Avatar size="sm" src={user?.avator} />
                </MenuButton>
                <MenuList zIndex="99">
                  <MenuItem>{user?.username}</MenuItem>
                  <MenuItem onClick={onClickSetting}>프로필 설정</MenuItem>
                  <MenuItem onClick={onMe}>내 정보</MenuItem>
                  <MenuItem onClick={onLogOut}>Log out</MenuItem>
                </MenuList>
              </Menu>
            )
          ) : null}
        </Box>
      </HStack>
    </Stack>
  );
}
