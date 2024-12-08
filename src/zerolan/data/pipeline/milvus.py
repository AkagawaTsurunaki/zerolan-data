from typing import List
from pydantic import BaseModel


class InsertRow(BaseModel):
    """
    Represents a row to be inserted into a Milvus database table.

    Attributes:
        id (int): Unique identifier for the row
        text (str): Text content of the row
        subject (str): Subject or category of the row
    """
    id: int
    text: str
    subject: str


class MilvusInsert(BaseModel):
    """
    Represents an insert operation for a Milvus collection.

    Attributes:
        collection_name (str): Name of the Milvus collection to insert into
        drop_if_exists (bool): Whether to drop the collection if it exists
        texts (List[InsertRow]): List of rows to be inserted
    """
    collection_name: str
    drop_if_exists: bool = False
    texts: List[InsertRow]


class MilvusInsertResult(BaseModel):
    """
    Represents the result of an insert operation on a Milvus collection.

    Attributes:
        insert_count (int): Number of rows successfully inserted
        ids (List[int]): IDs of the inserted rows
    """
    insert_count: int
    ids: List[int]


class MilvusQuery(BaseModel):
    """
    Represents a query operation on a Milvus collection.

    Attributes:
        collection_name (str): Name of the Milvus collection to query
        limit (int): Maximum number of results to return (top-k)
        output_fields (List[str]): Fields to include in the query results
        query (str): The actual query string
    """
    collection_name: str
    limit: int
    output_fields: List[str]
    query: str


class QueryRow(BaseModel):
    """
    Represents a row returned by a Milvus query.

    Attributes:
        id (int): Unique identifier for the row
        entity (dict): The actual data from the queried row
        distance (float): Distance metric used in the query
    """
    id: int
    entity: dict
    distance: float


class MilvusQueryResult(BaseModel):
    """
    Represents the result of a Milvus query operation.

    Attributes:
        result (List[List[QueryRow]]): Nested list containing all query results
    """
    result: List[List[QueryRow]]
