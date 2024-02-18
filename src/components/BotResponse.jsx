import React, { useEffect } from "react";
import { useState } from "react";
import Cardelem from "./CardElem";
import { Card, CardContent, CardMedia, Grid, Typography } from "@mui/material";

const BotResponse = ({ response, items, chatLogRef }) => {
  const [botResoponse, setBotResponse] = useState("");
  const [isPrinting, setIsPrinting] = useState(true);
  const [isButtonVisible, setIsButtonVisible] = useState(false);

  useEffect(() => {
    let index = 1;
    let msg = setInterval(() => {
      if (response !== " - The Ultimate AI Assistant") {
        setIsButtonVisible(true);
      }
      if (!isPrinting) {
        // if isPrinting is false, clear interval and return
        clearInterval(msg);
        return;
      }
      setBotResponse(response.slice(0, index));
      if (index >= response.length) {
        clearInterval(msg);
        setIsButtonVisible(false);
      }
      index++;

      // scroll to the bottom of the page whenever the messages array is updated
      if (chatLogRef !== undefined) {
        chatLogRef.current.scrollIntoView({
          behavior: "smooth",
          block: "end",
        });
      }
    }, 50);
    return () => clearInterval(msg); // clear interval on component unmount
  }, [chatLogRef, response, isPrinting]);

  const stopPrinting = () => setIsPrinting(!isPrinting);

  return (
    <>
      <pre id="#botresponse">
        {botResoponse}
        {botResoponse === response ? "" : "|"}
      </pre>
      <div>
        {items ? (
          <Grid container spacing={2}>
            {items.map((card) => (
              <Grid key={card.price} item xs={12} sm={6} md={4} lg={3}>
                <Card>
                  <CardMedia
                    component="img"
                    height="200"
                    width="200"
                    image={card.Image}
                    alt={card.NAme}
                  />
                  <CardContent>
                    <Typography variant="h5" component="div">
                      {card.Name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      {card.Price}
                    </Typography>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        ) : (
          <></>
        )}
      </div>
      {isButtonVisible && (
        <button className="stop-messgage" onClick={stopPrinting}>
          {isPrinting ? "Stop Message" : "Regenerate Message"}
        </button>
      )}
    </>
  );
};

export default BotResponse;
