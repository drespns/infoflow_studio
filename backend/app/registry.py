from app.transformations.load_csv import LoadCSVNode
from app.transformations.filter_rows import FilterRowsNode
from app.transformations.rename_column import RenameColumnNode
from app.transformations.groupby import GroupByNode


NODE_REGISTRY = {
    "load_csv": LoadCSVNode,
    "filter_rows": FilterRowsNode,
    "rename_column": RenameColumnNode,
    "group_by": GroupByNode,
}
