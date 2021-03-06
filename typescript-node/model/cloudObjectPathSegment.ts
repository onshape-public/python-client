/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class CloudObjectPathSegment {
    'cloudStorageProviderType'?: number;
    'cloudStorageAccountId'?: string;
    'name'?: string;
    'id'?: string;
    'treeHref'?: string;
    'resourceType'?: string;
    'subType'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "cloudStorageProviderType",
            "baseName": "cloudStorageProviderType",
            "type": "number"
        },
        {
            "name": "cloudStorageAccountId",
            "baseName": "cloudStorageAccountId",
            "type": "string"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "treeHref",
            "baseName": "treeHref",
            "type": "string"
        },
        {
            "name": "resourceType",
            "baseName": "resourceType",
            "type": "string"
        },
        {
            "name": "subType",
            "baseName": "subType",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return CloudObjectPathSegment.attributeTypeMap;
    }
}

