import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smoke-test")

def run_smoke_tests():
    try:
        from tools.list_models import list_models
        logger.info("list_models: %s", list_models())
    except Exception as e:
        logger.error("list_models failed: %s", e)

    try:
        from tools.get_fields import get_fields
        logger.info("get_fields: %s", get_fields("res.partner"))
    except Exception as e:
        logger.error("get_fields failed: %s", e)

    try:
        from tools.search_read import search_read
        logger.info("search_read: %s", search_read("res.partner", [["is_company", "=", True]], ["id", "name"], 1))
    except Exception as e:
        logger.error("search_read failed: %s", e)

    try:
        from tools.create_record import create_record
        logger.info("create_record: %s", create_record("res.partner", {"name": "Smoke Test"}))
    except Exception as e:
        logger.error("create_record failed: %s", e)

    try:
        from tools.update_record import update_record
        logger.info("update_record: %s", update_record("res.partner", [1], {"name": "Updated"}))
    except Exception as e:
        logger.error("update_record failed: %s", e)

    try:
        from tools.delete_record import delete_record
        logger.info("delete_record: %s", delete_record("res.partner", [1]))
    except Exception as e:
        logger.error("delete_record failed: %s", e)

    try:
        from tools.extract_parse import extract_parse
        logger.info("extract_parse: %s", extract_parse("dGVzdA==", "invoice", "18.0"))
    except Exception as e:
        logger.error("extract_parse failed: %s", e)

    try:
        from tools.extract_get_result import extract_get_result
        logger.info("extract_get_result: %s", extract_get_result("invoice", "18.0", "abc123"))
    except Exception as e:
        logger.error("extract_get_result failed: %s", e)

if __name__ == "__main__":
    run_smoke_tests()
