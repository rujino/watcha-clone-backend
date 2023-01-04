import { Box, Divider, Heading, Img, Text } from "@chakra-ui/react";
import styled from "styled-components";

const Space = styled.div`
  height: 56px;
  width: 100%;
`;

export default function Banner() {
  return (
    <Box paddingTop="65px">
      <Heading color="white">홈</Heading>
      <Divider mt="20px" mb="20px" />
      <Box display="flex">
        <Box margin="5px">
          <Text color="white">스테디셀러</Text>
          <Heading color="white">최고 인기작</Heading>
          <Text color="white">뭘 볼지 모르겠다면 여기서 골라보세요!</Text>
          <Img src="" w="523px" h="294px" />
        </Box>
        <Box margin="5px">
          <Text color="white">베스트 셀렉션</Text>
          <Heading color="white">오직 왓챠에서</Heading>
          <Text color="white">
            만나보는 독점 오리지널 & 익스클루시브 콘텐츠
          </Text>
          <Img src="" w="523px" h="294px" />
        </Box>
        <Box margin="5px">
          <Text color="white">새로 올라왔어요</Text>
          <Heading color="white">1월 1주 신작</Heading>
          <Text color="white">트립메이트: 후아유, 달이 지는 밤 등</Text>
          <Img src="" w="523px" h="294px" />
        </Box>
      </Box>
      <Space />
    </Box>
  );
}
