import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response=requests.get(url)
        response.raise_for_status()

        soup=BeautifulSoup(response.text, "html.parser")

        title=soup.title.string if soup.title else "No Title Found"
        paragragh=[p.get_text() for p in soup.find_all('p')]

        return title,paragragh
    except Exception as e:
        return None, [f"Error:{str(e)}"]
    

def main():
    st.title("Web Scrapping App")
    st.markdown(""""
    Enter a Url to scrape its content. This app will fetch 
                the webpage title and extract text from all paragraghs
                """)
    
    #Input for the url

    url=st.text_input("Enter the url:")

    if st.button("Scrape") and url:
        st.markdown("###Results:")

        #scrape the website
        title,paragragh=scrape_website(url)

        if title:
            st.markdown(f"**Title** {title}")
        else:
            st.markdown("**Title:** No Title found")

        st.markdown("**content:**")
        for para in paragragh:
            st.write(para)

if __name__=="__main__":
    main()