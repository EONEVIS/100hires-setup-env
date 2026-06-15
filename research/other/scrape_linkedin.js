import axios from 'axios';

const API_KEY = process.env.SCRAPECREATORS_API_KEY || 'YOUR_API_KEY_HERE';

async function fetchLinkedInPostContext(postUrl) {
  /**
   * Queries the ScrapeCreators API to retrieve structured text, engagement metrics,
   * and author metadata from specific public LinkedIn URLs.
   */
  const endpoint = `https://api.scrapecreators.com/v1/linkedin/post`;
  
  try {
    const response = await axios.get(endpoint, {
      params: { url: postUrl },
      headers: {
        'x-api-key': API_KEY,
        'Content-Type': 'application/json'
      }
    });
    
    if (response.data && response.data.success) {
      return {
        author: response.data.author.name,
        followers: response.data.author.followers,
        body: response.data.description,
        likes: response.data.likeCount,
        comments: response.data.commentCount,
        published: response.data.datePublished
      };
    }
  } catch (error) {
    console.error(`ScrapeCreators execution failed: ${error.response?.data || error.message}`);
    return null;
  }
}

// Running a test harvest against a verified public LinkedIn post
const samplePostUrl = 'https://www.linkedin.com/pulse/being-father-has-made-me-better-leader-vice-versa-austen-allred/';

console.log("Initializing ScrapeCreators extraction...");
fetchLinkedInPostContext(samplePostUrl).then(data => {
  if (data) {
    console.log("\n--- SCRAPE SUCCESSFUL ---");
    console.log(`Author: ${data.author} (${data.followers} followers)`);
    console.log(`Engagement: ${data.likes} Likes | ${data.comments} Comments`);
    console.log(`Snippet:\n"${data.body.substring(0, 300)}..."`);
  }
});