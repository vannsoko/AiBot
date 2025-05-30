
<!-- Anchor to the Top -->
<a name="readme-top"></a>




<h3 align="center">Ai Bot</h3>

  <p align="center">
Document Retrieval and Question Answering project using discord as interface and Vector Stores with openAI to efficiently handle, retrieve information from the context files and most important answer questions.   
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Document Retrieval and Question Answering project using discord as interface and Vector Stores with openAI to efficiently handle, retrieve information from the context files and most important answer questions.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* Disnake
* OpenAi

I'm using Discord as interface for the project, therefore I used Disnake to interact with the Discord API.
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- Docker
- Discord Bot Token

### Installation

1. Creat a free discord bot [Discord developers portal](https://discord.com/developers/applications) to get a bot token
2. Invite you new bot with admin permissions in your discord server
3. Clone the repo
   ```sh
   git clone https://github.com/vannsoko/AiBot.git
   ```
4. Renaming .env.exemple to .env
5. Enter BOT_TOKEN and START_CHANNEL_ID  in `.env`
   ```dotenv
    BOT_TOKEN="REPLACE THIS WITH THE BOT TOKEN FROM THE DISCORD DEVELOPERS PORTAL"
    START_CHANNEL_ID="START_CHANNEL ID WHERE THE BOT WILL BE INITIALIZED"
    OPENAI_API_KEY=""
    IN_DEV=true
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

1. Find an issue or create one your self. If you have create the issue please make sure that it is relevant to the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`). Please use the name of the issue in the branch name. or reference the issue id in the name.
3. Do your changes and commit them (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request and wait for it to be merged

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->



