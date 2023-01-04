import {
  Button,
  Container,
  Grid,
  GridItem,
  Heading,
  Text,
} from "@chakra-ui/react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import { adultPost, couponGet, couponPost } from "../api";
import useUser from "../lib/useUser";

const Space = styled.div`
  height: 56px;
  width: 100%;
`;

const InfoBox = styled.div`
  width: 100%;
  padding: 50px;
`;

interface ICoupon {
  id: number;
  username: string;
}

export default function MyPage() {
  const { user } = useUser();
  const { data: couponData } = useQuery<ICoupon>(["coupon"], couponGet);
  const navigator = useNavigate();
  const adultMutation = useMutation(adultPost, {
    onError: () => {
      console.log("adult error");
    },
  });
  const couponMutation = useMutation(couponPost, {
    onError: () => {
      console.log("coupon errors");
    },
  });
  const couponOnClick = () => {
    couponMutation.mutate();
    navigator("/home/me");
  };
  const adultOnClick = () => {
    const is_adult = true;
    adultMutation.mutate({ is_adult });
    navigator("/home/me");
  };
  console.log(couponData);
  return (
    <Container maxW="container.md">
      <InfoBox>
        <Heading color="white">설정</Heading>
        <Grid
          color="white"
          mt="30px"
          borderRadius="10px"
          templateColumns="1"
          templateRows="3"
        >
          <GridItem bgColor="#1B1B1C" h="40px" padding="10px" colSpan={1}>
            이용권
          </GridItem>
          <GridItem bgColor="#121314" h="94px" padding="10px" colSpan={1}>
            {couponData ? <Text>이용권 있음</Text> : <Text>이용권 없음</Text>}
          </GridItem>
          <GridItem bgColor="#121314" h="69px" padding="10px" colSpan={1}>
            {couponData ? null : (
              <Button bg="hidden" onClick={couponOnClick}>
                쿠폰 등록하기 &rarr;
              </Button>
            )}
          </GridItem>
        </Grid>
      </InfoBox>
      <Space />
      <InfoBox>
        <Grid color="white" templateColumns="1" templateRows="3">
          <GridItem bgColor="#1B1B1C" h="40px" padding="10px" colSpan={1}>
            계정
          </GridItem>
          <GridItem bgColor="#121314" h="94px" padding="10px" colSpan={1}>
            <Text>{user?.username}</Text>
          </GridItem>
          <GridItem bgColor="#121314" h="94px" padding="10px" colSpan={1}>
            {user?.is_adult ? (
              <Text>성인 인증 완료</Text>
            ) : (
              <Button bg="hidden" onClick={adultOnClick}>
                성인 인증 &rarr;
              </Button>
            )}
          </GridItem>
        </Grid>
      </InfoBox>
    </Container>
  );
}
