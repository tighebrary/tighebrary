import xml.etree.ElementTree as ET
from datetime import datetime
import create_episode

# Path to your RSS feed file
rss_file = "daily.xml"

# Load the RSS file
tree = ET.parse(rss_file)
root = tree.getroot()

# Create a new item element
new_item = ET.Element('item')

# Call the creat_audio.py script
# Get a new episode title, description, and audio file
episode = create_episode.new_episode()

# Add title, description, and other details to RSS item
title = ET.SubElement(new_item, 'title')
title.text = episode.title

description = ET.SubElement(new_item, 'description')
description.text = episode.description

pub_date = ET.SubElement(new_item, 'pubDate')
pub_date.text = episode.pub_date

enclosure = ET.SubElement(new_item, 'enclosure')
enclosure.set('url', episode.url)
enclosure.set('length', episode.length)
enclosure.set('type', episode.type)

guid = ET.SubElement(new_item, 'guid')
guid.text = episode.guid

# Append the new item to the channel
channel = root.find('channel')
channel.append(new_item)

# Save the updated RSS file
tree.write(rss_file, encoding="UTF-8", xml_declaration=True)
