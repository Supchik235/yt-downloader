import streamlit as st
from pytube import YouTube
from pathlib import Path
import streamlit_lottie as st_lottie
import json
st.set_page_config(page_title="InstallX",page_icon="Files/computer.png")
hide_st_style = """
            <style>
            #MainMenu {visibility: shown;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: none;
    height: 50px;
    width: 100%;
    padding: 5px;
    cursor: pointer;
    transition: 1.2s;
    
}
</style>""", unsafe_allow_html=True)
l = st.markdown("""
<style>
div.stButton > button:hover{
    
    position: centered;
    height: 55px;
    width: 100%;
    cursor: pointer;
    transition: 1.2s;
    
}
</style>""", unsafe_allow_html=True)


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)    
def main():
    tabs = ["YouTube Downloader", "Help"]

    tabs =  st.tabs(tabs)


                

    with tabs[0]:
        
        link = st.text_input("Enter Link to any YouTube video")
        options = ["Video","Audio"]
        quality_options = ["Highest","Lowest"]
        res = st.selectbox("Resolution:", options=quality_options)
        typ = st.selectbox("Type of video",options=options)
        path_selector = ["Downloads/","Desktop/","Documents/"]
        path1 = st.selectbox("Path:", options=path_selector)
        Button = st.button("Download")
        
        if Button:
            if len(link) == 0:
                st.error("Blank Line")
                Button = st.button("Click To Restart")
                if Button:
                    main()
            elif "www.youtube.com/watch" not in link:
                st.error("Not valid Youtube link")
                Button = st.button("Click To Restart")
                if Button:
                    main()
            else:
                if typ == "Video":
                    if res == "Highest":
                        with st.spinner("Downloading"):
                            url = YouTube(link)
                            video = url.streams.get_highest_resolution()
                            path = str(os.path.join(str(pathlib.Path.home()), path1))
                            
                            
                            video.download(path)
                        st.success("Done")
                    elif res == "Lowest":
                        with st.spinner("Downloading"):
                            
                            url = YouTube(link)
                            video = url.streams.get_lowest_resolution()
                            path = str(os.path.join(str(pathlib.Path.home()), path1))
                            
                            video.download(path)
                            
                elif typ == "Audio":
                    
                        with st.spinner("Downloading"):
                            url = YouTube(link)
                            video = url.streams.get_audio_only()
                            path = str(os.path.join(str(pathlib.Path.home()), path1))
                            video.download(path)
                            
                        st.success("Done")
            
    with tabs[1]:
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("Firstly Find a Youtube Video You Wan't to Watch")
            st.header("")
        with col2:
            st.image("Files/first.png")
        col3,col4 = st.columns(2)
        with col3:
            st.subheader("Now Copy The link")
        with col4:
            st.image("Files/third.png")
            st.header("")
        col5,col6 = st.columns(2)
        with col5:
            st.subheader("Paste The link into the Donwloader")
        with col6:
            st.image("Files/for.png")
            st.title("")
        col7,col8 = st.columns(2)
        with col7:
            st.subheader("After you made your settings press on the Download Button")
        with col8:
            st.image("Files/But.png")
            st.title("")
        col9,col10 = st.columns(2)
        with col9:
            st.subheader("After Some time the video will be ready")
        with col10:
            st.image("Files/Done.png")
            st.title("")
        col11,col12 = st.columns(2)
        with col11:
            st.subheader("You can find your video in the folder you selected")
        with col12:
            st.image("Files/end.png")
            st.title("")
        st.subheader("Enjoy!")
        
        


    


if __name__ == '__main__':
	main()
 
 
