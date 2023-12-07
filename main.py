import av
import streamlit as st
import cv2
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


class VideoTransformer(VideoTransformerBase):
  def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
    img = cv2.flip(img, 1)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

def main():
    st.title("WebRTC Example")
    webrtc_streamer(key="example", video_processor_factory=VideoTransformer)


if __name__ == "__main__":
    main()
