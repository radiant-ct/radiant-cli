from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_filter import ImageFilter
from ...models.image_response_dto import ImageResponseDTO
from ...types import UNSET, Response


def _get_kwargs(
    *,
    filter_: ImageFilter,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filter_ = filter_.to_dict()
    params.update(json_filter_)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/images",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[ImageResponseDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ImageResponseDTO.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ImageResponseDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: ImageFilter,
) -> Response[list[ImageResponseDTO]]:
    """
    Args:
        filter_ (ImageFilter):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ImageResponseDTO]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: ImageFilter,
) -> list[ImageResponseDTO] | None:
    """
    Args:
        filter_ (ImageFilter):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ImageResponseDTO]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: ImageFilter,
) -> Response[list[ImageResponseDTO]]:
    """
    Args:
        filter_ (ImageFilter):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ImageResponseDTO]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: ImageFilter,
) -> list[ImageResponseDTO] | None:
    """
    Args:
        filter_ (ImageFilter):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ImageResponseDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
        )
    ).parsed
