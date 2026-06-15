import os
import requests
import time

def extract_youtube_transcript(video_url: str, api_key: str) -> dict:
    """
    Programmatically extracts structured transcripts using the Supadata API,
    handling both direct transcript retrieval and asynchronous polling with Job IDs.
    """
    base_url = "https://api.supadata.ai/v1/transcript"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    params = {
        "url": video_url,
        "text": "true",  # Return plain text instead of timestamped chunks
        "mode": "auto"    # Fall back to AI transcription if native captions do not exist
    }
    
    response = requests.get(base_url, headers=headers, params=params)
    
    # Handle direct successful return (HTTP 200)
    if response.status_code == 200:
        return response.json()
    
    # Handle asynchronous polling trigger (HTTP 202 Accepted) for longer videos
    elif response.status_code == 202:
        job_data = response.json()
        job_id = job_data.get("jobId")
        poll_url = f"https://api.supadata.ai/v1/transcript/{job_id}"
        
        while True:
            poll_response = requests.get(poll_url, headers=headers)
            if poll_response.status_code == 200:
                return poll_response.json()
            elif poll_response.status_code == 206:
                # Job still processing, execute backoff to protect API limits
                time.sleep(10)
            else:
                raise Exception(f"Asynchronous transcribing failed: {poll_response.text}")
                
    else:
        raise Exception(f"API Request Failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Test URL from Mark Colgan's outbound training playlist
    test_video = "https://www.youtube.com/watch?v=sXcw6-wdrzA"
    api_key = os.environ.get("SUPADATA_API_KEY", "YOUR_API_KEY_HERE")
    
    print(f"Connecting to Supadata API to transcribe: {test_video}...")
    try:
        data = extract_youtube_transcript(test_video, api_key)
        print("\n--- TRANSCRIPT EXTRACTED SUCCESSFULLY ---")
        print(data.get("content", "No content field returned.")[:500] + "...")
    except Exception as e:
        print(f"\nExecution terminated: {e}")