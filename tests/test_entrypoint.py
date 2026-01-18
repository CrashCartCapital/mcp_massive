def test_entrypoint_exports_server():
    import entrypoint
    from mcp_massive.server import poly_mcp

    assert entrypoint.server is poly_mcp
