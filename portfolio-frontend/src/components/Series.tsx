import { Box, Button, Heading, HStack } from "@chakra-ui/react";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { FaPlayCircle, FaPlusCircle } from "react-icons/fa";
import styled from "styled-components";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import {
  countPlayCount,
  getSeriesDetail,
  getWishlist,
  plusToggle,
} from "../api";
import { ISeriesDetail, IWishlist } from "../types";
import { useState } from "react";

const CardVariants = {
  normal: {
    scale: 1,
  },
  hover: {
    scale: 1.1,
  },
};

const InfoVariants = {
  hover: {
    opacity: 1,
  },
};

const brightVariants = {
  hover: {
    opacity: 1,
  },
};

const Card = styled(motion.div)`
  width: 190px;
  height: 280px;
  background-color: gray;
  margin-top: 15px;
  margin-bottom: 15px;
  background-image: url("https://an2-img.amz.wtchn.net/image/v2/dRe-8K8ftG99FomnVUANUw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk56STVlREV3T0RCeE9EQWlYU3dpY0NJNklpOTJNaTl6ZEc5eVpTOXBiV0ZuWlM4eE5qVXpPVFkwTXpjek1qY3pNVFV6TnpZMEluMC5oeVNPcXpBSWpWMVgxUGUzLU9WdzNRWFl5ZnljMDVCQzB5dUVld0t4Mnhv");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  border-radius: 10px;
  position: relative;
`;

const Info = styled(motion.div)`
  padding: 20px;
  opacity: 0;
  bottom: 0;
  position: absolute;
  width: 100%;
  z-index: 5000;
`;

const BrightBox = styled(motion.div)`
  width: 100%;
  height: 100%;
  background-image: url("https://an2-img.amz.wtchn.net/image/v2/dRe-8K8ftG99FomnVUANUw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk56STVlREV3T0RCeE9EQWlYU3dpY0NJNklpOTJNaTl6ZEc5eVpTOXBiV0ZuWlM4eE5qVXpPVFkwTXpjek1qY3pNVFV6TnpZMEluMC5oeVNPcXpBSWpWMVgxUGUzLU9WdzNRWFl5ZnljMDVCQzB5dUVld0t4Mnhv");
  background-color: black;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  border-radius: 10px;
  filter: brightness(50%);
  opacity: 0;
  position: absolute;
`;

export interface ISeriesTinyProp {
  id: number;
  title: string;
  genre: string;
  possible_age: string;
  poster_url: string;
  is_interested: boolean;
}

export default function Series({
  id,
  title,
  genre,
  possible_age,
  poster_url,
  is_interested,
}: ISeriesTinyProp) {
  const { data } = useQuery<IWishlist[]>(["wishlist"], getWishlist, {
    retry: false,
  });
  const { data: seriesData } = useQuery<ISeriesDetail>(
    ["series", id],
    getSeriesDetail
  );
  const [value, setValue] = useState(is_interested);
  const queryClient = useQueryClient();
  const mutation = useMutation(plusToggle, {
    onSuccess: () => {
      console.log("good");
      queryClient.refetchQueries(["series"]);
      queryClient.refetchQueries(["seriesDrama"]);
      queryClient.refetchQueries(["wishlist"]);
    },
    onError: () => {
      console.log("nono");
    },
  });
  const countMutation = useMutation(countPlayCount, {
    onSuccess: () => {
      console.log("count");
    },
  });
  const interestedButtonClick = (
    event: React.SyntheticEvent<HTMLButtonElement>
  ) => {
    event.preventDefault();
    setValue(!value);
    const seriesPk = id;
    const userPk = data?.[0].id as number;
    console.log("userPk = ", userPk);
    console.log("seriesPk = ", seriesPk);
    mutation.mutate({ userPk, seriesPk });
  };
  const playButtonClick = (event: React.SyntheticEvent<HTMLButtonElement>) => {
    event.preventDefault();
    const videoPk = seriesData?.video[0].pk;
    console.log(seriesData?.video[0].sub_title);
    countMutation.mutate({ videoPk });
    console.log("!");
  };
  return (
    <Link to={`/home/series/${id}`}>
      <Card variants={CardVariants} initial="normal" whileHover="hover">
        <BrightBox variants={brightVariants}></BrightBox>
        <Info variants={InfoVariants}>
          <HStack marginBottom="10px">
            <Button
              color="white"
              onClick={playButtonClick}
              bgColor="transparent"
              variant="link"
            >
              <FaPlayCircle style={{ fontSize: "35px" }} />
            </Button>
            <Button
              color="white"
              onClick={interestedButtonClick}
              bgColor="transparent"
              p="0"
              variant="link"
            >
              {is_interested ? (
                <FaPlusCircle style={{ fontSize: "35px", color: "red" }} />
              ) : (
                <FaPlusCircle
                  style={{
                    fontSize: "35px",
                  }}
                />
              )}
            </Button>
          </HStack>
          <HStack marginBottom="10px">
            <Heading fontSize="20px" style={{ color: "white" }}>
              {title}
            </Heading>
            <Box>{possible_age}</Box>
          </HStack>
          <Box style={{ color: "white" }}>{genre}</Box>
        </Info>
      </Card>
    </Link>
  );
}
