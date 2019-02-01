# Device Regisrty Service

## Usage

All response will have the form

```json
{
        "data": "Mixed type holding the content of the response",
        "message": "Description of what happened"
}
```

Submit response definitions will only detail the expected value of the `data field`

### List all devices

**Definition**

`GET /devices`
**Response**

-`200 OK` on success

```json
[
  {
    "identifier": "floor-lamp",
    "name": "Floor lamp",
    "device_type": "switch",
    "controller_gateway": "192.2.41.1."
  }
  {
    "identifier": "samsung-tv",
    "name": "Living Room TV",
    "device_type": "tv",
    "controller_gateway": "192.168.0.2."
  }
]
```

### Registering a new device
 **Definition**

 `POST /devices`


**Arguments**

- `"identifier":string` a globally new identifier for this device
- `"name":string` a friendly name for this device
- `"device_type": string` the type of the device as understood by the client
- `"controller_gateway": string` the IP address

If a device with the given identifier already exists, the existing device will be overwritten

**Response**

- `201 Created` on success
```json
{
  "identifier": "floor-lamp",
  "name": "Floor lamp",
  "device_type": "switch",
  "controller_gateway": "192.2.41.1."
}
```

## Lookup device details

`GET /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
  "identifier": "floor-lamp",
  "name": "Floor lamp",
  "device_type": "switch",
  "controller_gateway": "192.2.41.1."
}
```

## Delete a device

**Definition**

`DELETE /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success
