
# API paths

:swg-path: /pet
    verbs:
      - post
      - get

:swg-path: /pet/{petId}/uploadImage
    verbs:
      - post
      - get
    sections:
      parameters: true
      responseTables: true
      responseExamples: true

:swg-path: /pet/findByStatus

:swg-path: /pet/findByTags

:swg-path: /pet/{petId}
    verbs:
      - delete

:swg-path: /store/order

:swg-path: /store/order/{orderId}

:swg-path: /store/inventory

:swg-path: /user/createWithArray

:swg-path: /user/createWithList

:swg-path: /user/{username}

:swg-path: /user/login

:swg-path: /user/logout

:swg-path: /user

# Definitions

## Pet definition

:swg-def: Pet

## User definition

:swg-def: User

## Orfer definition

:swg-def: Order

## Tag definition

:swg-def: Tag

## ApiResponse

:swg-def: ApiResponse
