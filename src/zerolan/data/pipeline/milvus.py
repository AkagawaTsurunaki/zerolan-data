from typing import List

from pydantic import BaseModel, Field


class InsertRow(BaseModel):
    """
    Represents a row to be inserted into a Milvus database table.
    """
    id: int = Field(..., description="Unique identifier for the row.")
    text: str = Field(..., description="Text content of the row.")
    subject: str = Field(..., description="Subject or category of the row.")


class MilvusInsert(BaseModel):
    """
    Represents an insert operation for a Milvus collection.
    """
    collection_name: str = Field(..., description="Name of the Milvus collection to insert into.")
    drop_if_exists: bool = Field(False, description="Whether to drop the collection if it exists.")
    texts: List[InsertRow] = Field(..., description="List of rows to be inserted.")


class MilvusInsertResult(BaseModel):
    """
    Represents the result of an insert operation on a Milvus collection.
    """
    insert_count: int = Field(..., description="Number of rows successfully inserted.")
    ids: List[int] = Field(..., description="IDs of the inserted rows.")


class MilvusQuery(BaseModel):
    """
    Represents a query operation on a Milvus collection.
    """
    collection_name: str = Field(..., description="Name of the Milvus collection to query.")
    limit: int = Field(..., description="Maximum number of results to return (top-k).")
    output_fields: List[str] = Field(..., description="Fields to include in the query results.")
    query: str = Field(..., description="The actual query string.")


class QueryRow(BaseModel):
    """
    Represents a row returned by a Milvus query.
    """
    id: int = Field(..., description="Unique identifier for the row.")
    entity: dict = Field(..., description="The actual data from the queried row.")
    distance: float = Field(..., description="Distance metric used in the query.")


class MilvusQueryResult(BaseModel):
    """
    Represents the result of a Milvus query operation.
    """
    result: List[List[QueryRow]] = Field(..., description="Nested list containing all query results.")
