# Subtitle-Translation-Service
Subtitle Translation Service using Google translation and opensubtitles.org

# Work in progress 

Required for Google script:

pip install google-cloud-translate googletrans pysubs2

Usage for Google script:

Replace path/to/your/credentials.json with the path to your Google Cloud credentials file.

Replace path/to/your/subtitle.srt with the path to your SRT file.

Set the target_language to the language you want to translate the subtitles into.
Run the script.


Usage for Kodi script:

Replace placeholders: Update PLUGIN_ID and other constants with your plugin's details.

Implement plugin logic: Fill in the show_root_list, handle_listing, and play_item functions with your plugin's specific functionality.

Refer to Kodi documentation: Consult the official Kodi documentation for detailed usage of the Kodi API functions used in the stub.