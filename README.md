> May As Well Learn MarkDown While I'm At It (tm)


# eveBackend

This script will hold all backend code for the EVE Market Analyser.
It will be hostable (hopefully) on nginx or apache, once finished.

## Requirements:
* locally hosted mysql database for the SDE
* python3
* flask
* mysql-connector

The backend will be able to, for a particular location, search the
region and adjacent regions for items and find price disparities. 
For each disparity, it should be able to calculate the most profitable
buy and sell pair using ISK/jump, required collateral, volume, and 
low-sec risk. Limits for the jump count should be an option to avoid
huge treks.

## TODO:
#### Basic API endpoints

1. Items

  - [x] Convert item ID to name
  - [x] Convert item name to ID
  - [ ] Get item group ID for an item by ID
  - [ ] Get item group name for an item by ID
  - [ ] Get item group ID for an item by name
  - [ ] Get item group name for an item by name
  - [ ] Get a list of item IDs in a group by group name
  - [ ] Get a list of item names for a group by group ID	
  - [ ] Get a list of ID/name pairs for a group by group name
  - [ ] Get a list of ID/name pairs for a group by group ID

1. Regions
  - [ ] Convert region ID to name
  - [ ] Convert region name to ID
  - [ ] Get adjacent region names for a region by name
  - [ ] Get adjacent region IDs for a region by name
  - [ ] Get adjacent region ID/name pairs for a region by name
  - [ ] Get adjacent region names for a region by ID
  - [ ] Get adjacent region IDs for a region by ID
  - [ ] Get adjacent region ID/name pairs for a region by ID
  - [ ] Get list of system IDs for a region by ID
  - [ ] Get list of system names for a region by ID
  - [ ] Get list of system ID/name pairs for a region by ID

1. Systems

  - [ ] Convert system ID to name
  - [ ] Convert system name to ID

1. Market Buy Orders

  - [ ] Get a list of buy orders for an item ID by region ID
  - [ ] Get a list of buy orders for an item ID by region name
  - [ ] Get a list of buy orders for an item name by region ID
  - [ ] Get a list of buy orders for an item name by region name
  - [ ] Get a list of buy orders for an item group ID by system ID
  - [ ] Get a list of buy orders for an item group ID by system name
  - [ ] Get a list of buy orders for an item group name by system ID
  - [ ] Get a list of buy orders for an item group name by system name

1. Market Sell Orders

  - [ ] Get a list of sell orders for an item ID by region name
  - [ ] Get a list of sell orders for an item ID by region ID
  - [ ] Get a list of sell orders for an item name by region ID
  - [ ] Get a list of sell orders for an item name by region name
  - [ ] Get a list of sell orders for an item group ID by system ID
  - [ ] Get a list of sell orders for an item group ID by system name
  - [ ] Get a list of sell orders for an item group name by system ID
  - [ ] Get a list of sell orders for an item group name by system name

1. Item Details

  - [ ] Get a list of item details for an item ID
  - [ ] Get a list of item details for an item name
  - [ ] Get volume of item by ID
  - [ ] Get volume of item by name
  - [ ] Get description of item by ID
  - [ ] Get description of item by name
  - [ ] Get item group of item by ID (redirect to /api/item)
  - [ ] Get item group of item by name
  - [ ] Get skill requirements of item by ID
  - [ ] Get skill requirements of item by namy
  - [ ] Get manufacturing requirements of item by ID (recursive?)
  - [ ] Get manufacturing requirements of item by name (recursive?)
	
