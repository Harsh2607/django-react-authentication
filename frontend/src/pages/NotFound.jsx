import { Link } from "react-router-dom";

const NotFound = () => {
    return (
        <div className="min-h-screen flex flex-col items-center justify-center">
            <h1 className="text-9xl font-bold">404</h1>
            <p className="text-3xl font-light">Page not found</p>
            <Link to="/" className="text-blue-500 underline mt-4">
                Go back home
            </Link>
        </div>
    );
};

export default NotFound;
